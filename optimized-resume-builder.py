import argparse
import subprocess
import time
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
import html5lib

# creates optimized resuem bullets within a pdf document using keywords
# from the job posting to speed up the time to make a resume for each job 

# future create a stream of sites that create an individual resume for each posting
def optimized_resume_builder():
    #runs bash script
    run_bash_script()
    args = get_command_line_args()

    """ html = urlopen(args.url) 
    soup = BeautifulSoup(html)
    print(soup, "html doc") """
    
    with urlopen(args.url) as f:
        soup = BeautifulSoup(f)
        print(soup)
    """ with urlopen(args.url) as f:
        document = html5lib.parse(f, transport_encoding=f.info().get_content_charset())
       
        soup.find("element")
        print(document) """

    

    print(args.filename, args.url)
# uses subprocesses to run bash script     
def run_bash_script():
    rc = subprocess.Popen(['bash', './cli_font.sh'])
    time.sleep(5)
    rc.terminate()
    rc.wait()
    print("done")

# gets command line arguments for resume and the url for job posting
def get_command_line_args():
    parser = argparse.ArgumentParser("Tool to build a resume from a job description using GPT")
    parser.add_argument('filename', 
                    help='file for the cli resume')
    parser.add_argument('url', 
                    help='url for the jobsite description')
    


    args = parser.parse_args()
    return args

    




if __name__ == '__main__':
    optimized_resume_builder()
    