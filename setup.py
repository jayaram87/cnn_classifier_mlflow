from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    desc = f.read()

setup(
    name='REPO_NAME',
    version='0.0.1',
    author='Jay Raja',
    description='sample MLFLOW CNN app',
    long_description=desc,
    long_description_content_type='text/markdown',
    url='https://github.com/jayaram87/{REPO_Name}',
    author_email='jayaramraja1987@gmail.com',
    packages=['src'],
    license='MIT',
    python_requires='>=3.7',
    install_requirements=[
        'tensorflow',
        'keras',
        'numpy',
        'tqdm',
        'PyYAML',
        'mlflow'
    ]
)