from src.jobs import read


def get_unique_job_types(path: str):
    data_jobs = read(path)
    unique_job_types = []
    for job in data_jobs:
        if job['job_type'] not in unique_job_types:
            unique_job_types.append(job['job_type'])
    return unique_job_types

    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """


def get_unique_industries(path):
    data_jobs = read(path)
    unique_industries = []
    for job in data_jobs:
        if job['industry'] not in unique_industries:
            if job['industry'] != '':
                unique_industries.append(job['industry'])
    return unique_industries

    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
    Must be passed to `read`

    Returns
    -------
    list
    List of unique industries
    """


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    data_jobs = read(path)
    max_salary_list = []
    for job in data_jobs:
        if job['max_salary'] not in max_salary_list:
            if job['max_salary'] != '' and job['max_salary'].isdigit():
                max_salary_list.append(int(job['max_salary']))
                max_salary = max(max_salary_list)
    return max_salary
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    pass


def get_min_salary(path):
    data_jobs = read(path)
    min_salary_list = []
    for job in data_jobs:
        if job['min_salary'] not in min_salary_list:
            if job['min_salary'] != '' and job['min_salary'].isdigit():
                min_salary_list.append(int(job['min_salary']))
                min_salary = min(min_salary_list)
    return min_salary
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
