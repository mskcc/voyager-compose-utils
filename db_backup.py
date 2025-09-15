import os
import sys
import glob
import logging
import subprocess
from datetime import datetime

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)


def dump_postgres(pg_dump, host, port, db_name, username, filename):
    f = open(filename, "w")
    dump_postgres_command = (
        pg_dump,
        "-Z7",
        "-Fc",
        "-h",
        "%s" % host,
        "-p",
        "%s" % port,
        "-U",
        "%s" % username,
        "%s" % db_name,
    )
    logging.info("Running backup with command %s" % str(dump_postgres_command))
    return_code = subprocess.call(dump_postgres_command, stdout=f)
    if return_code != 0:
        logging.error("Backup failed")
    else:
        logging.info("Backup successfully finished to location: %s" % filename)


def backup(
    basename, directory, max_backups, pg_dump_command, host, port, db_name, username
):
    logging.info("Starting backup")
    if not os.path.exists(directory):
        logging.info("Creating backup directory %s" % directory)
        os.mkdir(directory)
    logging.info("Listing backups in %s" % directory)
    files = list(filter(os.path.isfile, glob.glob(directory + "/*")))
    files.sort(key=lambda x: os.path.getmtime(x))
    logging.info("Current number of backups %s" % len(files))
    if len(files) == max_backups:
        file_to_remove = files.pop(0)
        logging.info("Removing previous file %s" % file_to_remove)
        os.remove(file_to_remove)
    filename = "%s_%s" % (basename, datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f"))
    filepath = os.path.join(directory, filename)
    dump_postgres(pg_dump_command, host, port, db_name, username, filepath)


if __name__ == "__main__":
    HELP_MESSAGE = """
    Help:
    python db_backup.py <basename> <directory> <max_backups> <pg_dump_command> <postgres_host> <postgres_port> <database_name> <username>
    _______________________
    error: %s
    """
    try:
        if len(sys.argv) != 9:
            raise Exception("Invalid number of arguments")
        basename = sys.argv[1]
        directory = sys.argv[2]
        max_backups = int(sys.argv[3])
        pg_dump_command = sys.argv[4]
        postgres_host = sys.argv[5]
        postgres_port = sys.argv[6]
        database_name = sys.argv[7]
        username = sys.argv[8]
    except Exception as e:
        print(HELP_MESSAGE % str(e))
    else:
        backup(
            basename,
            directory,
            max_backups,
            pg_dump_command,
            postgres_host,
            postgres_port,
            database_name,
            username,
        )
