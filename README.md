# GitHub Events Analyzer (Zally)

GitHub Events Analyzer is a Python script that analyzes events from a GitHub repository using the GitHub Events API.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/github-events-analyzer.git
```

2. Navigate to the project directory:

```bash
cd Zally_Assesment
```

3. install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Execute the script with the desired options:

```python
python manin.py
```

OR


```python
python main.py --owner <repo_owner> --repo <repo_name> --event_type <event_type> --page <page_number> --sort_order <sort_order>
```

Replace the following parameters:

a. `<repo_owner> (mandatory if repo_name is given)`: The owner of the GitHub repository.\
b. `<repo_name> (mandatory if repo_owner is given)`: The name of the GitHub repository.\
c. `<event_type> (optional)`: Filter events by type.\
d. `<page_number> (optional)`: The page number for pagination.\
e. `<sort_order> (optional)`: The sort order for events. Valid options are "chronological" or "reverse-chronological".


### Cheers!