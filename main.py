from scripts.download_files import download_file, get_file_list

def main():
    files = get_file_list()
    for file in files:
        download_file(file)

if __name__ == "__main__":
    main()