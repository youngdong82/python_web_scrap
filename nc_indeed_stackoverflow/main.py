from indeed import get_jobs as get_indeed_jobs
from stack import get_jobs as get_stack_jobs
from save import save_to_file

stack_jobs = get_stack_jobs()
indeed_jobs = get_indeed_jobs()
jobs = stack_jobs + indeed_jobs
save_to_file(jobs)