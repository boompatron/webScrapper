from indeed import get_job as get_indeed_jobs


def main():
    indeed_jobs = get_indeed_jobs()
    print(indeed_jobs)


if __name__ == "__main__":
    main()
