# SOFORT

SOftware FORum Tool: A StackOverflow lookalike to ask questions amongst a group of developers.

## Getting started

SOFORT is a tool that looks very much like StackOverflow.

At Arcelor Mittal Ghent, the Python support team is looking for a tool similar to StackOverflow to support the users working with Python, Jupyter, Pandas, ...  At the start of this project, this was done in Teams.  But information is lost and Teams is not searchable, amongst other problems.  

StackOverflow was considered as the tool, but after negotiations, Arcelor Mittal did not come to an agreement.

Another tool was investigated: biostar-forum.  This tool does pretty much what it is needed, however, it has some problems and they can not easily be overcome, nor is there much help from the community.  Furthermore, I (vindevoy) did not like the coding style that much.  I am used to a much stricter style.  Nor do I support all the technical decisions, for instance the HTML framework.

Therefore, this tool is created to have a something like StackOverflow, heavily inspired on the biostar-forum.


## Technology stack

- Python (3.10)
- Django
- MS SQL Server: Arcelor Mittal is only using this RDBMS (along DB2 and Oracle for other type of projects) for this kind of solutions.  Django is using other databases also, but the main focus during the development is Microsoft SQL Server.
- Poetry: poetry is elected over conda (/miniconda) for dependency handling.


## Authors

- Yves Vindevogel (vindevoy on GitLab, sidviny on Arcelor Mittal)


## License

To be discussed together with Arcelor Mittal.  For now, it's copyrighted.


## Project status

This project has just started.  There's not even an alpha version yet.

### Side note

This project is developed alongside another project that I (vindevoy) develop (Clivia Blog).  The rapid start of this project is based on the work that already exists on that tool.