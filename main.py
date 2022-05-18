from indeed import extract_indeed_pages, extract_indeed_jobs


def main():
    last_indeed_page = extract_indeed_pages()
    extract_indeed_jobs(last_indeed_page)


if __name__ == "__main__":
    main()
