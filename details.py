from github import Github
import base64

# create a Github instance
g = Github()

# get the repository
repo = g.get_repo('OWNER/REPO')

# get the languages used in the repository
languages = repo.get_languages()

# print the languages and their usage percentages
print('Languages:')
for language in languages:
    print(language + ': ' + str(languages[language]) + '%')

# get the contents of requirements.txt
try:
    contents = repo.get_contents('requirements.txt')
    # decode the content to a string
    content_string = base64.b64decode(contents.content).decode('utf-8')
    # split the string by newlines to get a list of dependencies
    dependencies = content_string.split('\n')
    # print the dependencies
    print('\nDependencies:')
    for dependency in dependencies:
        print(dependency)
except:
    print('\nNo requirements.txt found')

# look for the use of specific frameworks
frameworks = ['django', 'flask', 'react', 'angular']
print('\nFrameworks:')
for framework in frameworks:
    if framework in repo.get_topics():
        print(framework)

# examine the project's build scripts
build_files = ['Makefile', 'build.gradle', 'pom.xml']
print('\nBuild Tools:')
for build_file in build_files:
    try:
        contents = repo.get_contents(build_file)
        print(build_file)
    except:
        pass

# examine the project's test files and configurations
test_files = ['pytest.ini', 'setup.cfg', 'tox.ini']
print('\nTesting Tools:')
for test_file in test_files:
    try:
        contents = repo.get_contents(test_file)
        print(test_file)
    except:
        pass

# examine the project's configuration files for database information
db_files = ['config.yaml', 'settings.py']
print('\nDatabases:')
for db_file in db_files:
    try:
        contents = repo.get_contents(db_file)
        if 'mysql' in contents.decoded_content.decode('utf-8') or 'postgres' in contents.decoded_content.decode('utf-8'):
            print(db_file)
    except:
        pass
