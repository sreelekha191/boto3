import git

# clone the repository
repo_url = "https://github.com/sreelekha191/boto3.git"
repo_path = "/Users/sreelekha/Documents/GitHub/boto3"
repo = git.Repo.clone_from(repo_url,repo_path)

#checkout the branch to be deleted
branch_name="my_branch"
repo.git.chechkout(test)

#Merge the branch into the master branch_name
repo.git.merge(branch_name)

Delete the branch
repo.git.branch("-d",branch_name)

#push the change to the remote repository
repo.git.push("origin","master")
