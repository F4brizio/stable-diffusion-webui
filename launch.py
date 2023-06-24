from modules import launch_utils

args = launch_utils.args
python = launch_utils.python
git = launch_utils.git
index_url = launch_utils.index_url
dir_repos = launch_utils.dir_repos

commit_hash = launch_utils.commit_hash
git_tag = launch_utils.git_tag

run = launch_utils.run
is_installed = launch_utils.is_installed
repo_dir = launch_utils.repo_dir

run_pip = launch_utils.run_pip
check_run_python = launch_utils.check_run_python
git_clone = launch_utils.git_clone
git_pull_recursive = launch_utils.git_pull_recursive
run_extension_installer = launch_utils.run_extension_installer
prepare_environment = launch_utils.prepare_environment
configure_for_tests = launch_utils.configure_for_tests
start = launch_utils.start

import threading
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        print(f"Se ha creado un nuevo archivo: {event.src_path}")


def start_observer(path):
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


def main():
    print("Iniciando... main()")
    path = "/kaggle/working/stable-diffusion-webui/tmp/"  # Ruta que deseas monitorear

    observer_thread = threading.Thread(target=start_observer, args=(path,))
    observer_thread.start()
    print("observer_thread... start()")

    path2 = "/kaggle/working/stable-diffusion-webui/outputs/"  # Ruta que deseas monitorear

    observer_thread2 = threading.Thread(target=start_observer, args=(path2,))
    observer_thread2.start()
    print("observer_thread2... start()")

    print("Iniciando... v0.2 f4brizio")

    if not args.skip_prepare_environment:
        prepare_environment()

    if args.test_server:
        configure_for_tests()

    start()


if __name__ == "__main__":
    main()
