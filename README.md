
# PSNA Project

This project is designed to collect and log system performance metrics such as CPU usage, memory usage, and disk I/O statistics. It's useful for monitoring and analyzing the performance of a system over time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3
- pip (Python package manager)
- Git (for cloning the repository)

### Installation

1. **Clone the Repository**

   First, clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/B-Nageshwari/psna_project.git
   ```

2. **Navigate to the Project Directory**

   Change to the project directory:

   ```bash
   cd psna_project
   ```

3. **Set Up a Virtual Environment (Optional)**

   It's recommended to use a virtual environment to avoid conflicts with other projects or system-wide Python packages. Create a virtual environment:

   ```bash
   python -m venv virt
   ```

   Activate the virtual environment:

   - On Windows:
     ```bash
     .\virt\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source virt/bin/activate
     ```

4. **Install Required Packages**

   Install all the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

After installation, you can run the project:

```bash
python main.py
```

This script will start collecting system metrics and save them to a CSV file at regular intervals.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/B-Nageshwari/psna_project/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Swathika** - *Initial work*

See also the list of [contributors](https://github.com/B-Nageshwari/psna_project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/B-Nageshwari/psna_project/LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
