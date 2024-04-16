import shutil
from pathlib import Path
from multiprocessing.pool import ThreadPool
import multiprocessing


def copy_file(src_file, dst_dir):
    try:
        shutil.copy(src_file, dst_dir)
        print(f"Copied {src_file} to {dst_dir}")
    except Exception as e:
        print(f"Error copying {src_file}: {e}")

def process_directory(src_dir, dst_dir):
    try:
        src_path = Path(src_dir)
        dst_path = Path(dst_dir)

        for src_file in src_path.rglob('*'):
            if src_file.is_file():
                file_extension = src_file.suffix.lower()
                target_dir = dst_path / file_extension.strip('.')
                target_dir.mkdir(parents=True, exist_ok=True)
                copy_file(src_file, target_dir)
    except Exception as e:
        print(f"Error processing directory {src_dir}: {e}")

def main(src_dir, dst_dir):
    dst_path = Path(dst_dir)
    dst_path.mkdir(parents=True, exist_ok=True)

    num_threads = multiprocessing.cpu_count()
    pool = ThreadPool(num_threads)

    try:
        pool.starmap(process_directory, [(src_dir, dst_dir)])
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pool.close()
        pool.join()

if __name__ == "__main__":
    source_directory = input("Enter source directory path: ")
    destination_directory = input("Enter destination directory path: ")
    main(source_directory, destination_directory)
