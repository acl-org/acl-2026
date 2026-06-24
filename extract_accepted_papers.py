#!/usr/bin/env python

import csv
import sys

if len(sys.argv) < 2:
  print('Usage:\nextract_accepted_papers.py [path to csv file containing all accepted papers]')
  sys.exit()

cl_papers = []
tacl_papers = []
main_papers = []
industry_papers = []
srw_papers = []
demo_papers = []
findings_papers = []

with open(sys.argv[1]) as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    try:
      paper_id_col = row.index('Paper number')
      paper_title_col = row.index('Title')
      paper_authors_col = row.index('Authors Names')
      print('Found header row.')
      break
    except ValueError:
      paper_id_col = -1

  if paper_id_col == -1:
    print('ERROR: Unable to find header row.')
    sys.exit()

  min_column_count = max(paper_id_col, paper_title_col, paper_authors_col)
  num_papers_extracted = 0
  for row in reader:
    if len(row) <= min_column_count:
      print(f'WARNING: Found row with too few columns.')
      print(row)
      continue

    paper_id = row[paper_id_col].strip()
    title = row[paper_title_col].strip()
    authors = row[paper_authors_col].strip()

    if authors[-1] == ';':
      authors = authors[:-1]

    try:
      paper_type = paper_id[paper_id.index('-')+1:]
    except ValueError:
      print(f'WARNING: Paper with ID "{paper_id}" has invalid "Paper number" format.')
      print(f'  Title: {title}')
      print(f'  Authors: {authors}')
      continue

    if paper_type == 'CL':
      cl_papers.append((title, authors))
    elif paper_type == 'TACL':
      tacl_papers.append((title, authors))
    elif paper_type == 'MAIN':
      main_papers.append((title, authors))
    elif paper_type == 'IND':
      industry_papers.append((title, authors))
    elif paper_type in ('SRW', 'SRW-A'):
      srw_papers.append((title, authors))
    elif paper_type == 'DEMO':
      demo_papers.append((title, authors))
    elif paper_type == 'FIND':
      findings_papers.append((title, authors))
    else:
      print(f'WARNING: Unrecognized paper type in paper ID "{paper_id}".')
      print(f'  Title: {title}')
      print(f'  Authors: {authors}')
      continue
    num_papers_extracted += 1

  print(f'Successfully extracted {num_papers_extracted} papers.')

def write_papers_to_yml(papers, ymlpath):
  num_papers_written = 0
  with open(ymlpath, 'w') as outfile:
    for title, authors in papers:
      outfile.write(f'- title: {title}\n')
      outfile.write(f'  authors: {authors}\n')
      num_papers_written += 1
    print(f'Successfully wrote {num_papers_written} papers to "{ymlpath}".')

write_papers_to_yml(cl_papers, '_data/papers_cl.yml')
write_papers_to_yml(tacl_papers, '_data/papers_tacl.yml')
write_papers_to_yml(main_papers, '_data/papers_main.yml')
write_papers_to_yml(industry_papers, '_data/papers_industry.yml')
write_papers_to_yml(srw_papers, '_data/papers_srw.yml')
write_papers_to_yml(demo_papers, '_data/papers_demo.yml')
write_papers_to_yml(findings_papers, '_data/papers_findings.yml')
