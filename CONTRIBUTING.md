All contributions are welcome and appreciated. The project uses the
[general guidelines](https://guides.github.com/introduction/flow/)
for the fork-branch-pull request model for github.

1. Make sure your fork's `main` branch is up to date:

    	git remote add anirudhpnbb https://github.com/anirudhpnbb/Pyostie.git
        git checkout main
        git pull

2. Start a feature branch with a descriptive name about what you're
   trying to accomplish:

        git checkout -b docx_insights

3. Make commits to this feature branch (`docx_insights`, in this case)
   in a way that other people can understand with good commit messages
   to explain the changes you've made:
   
	    git add Pyostie/pyostie/docx_insights.py
	    git commit -m 'docx_insights updated.'

4. If the issue doesn't already exist, just send a pull
   request in the usual way:

    git push origin docx_insights
		http://github.com/anirudhpnbb/Pyostie/compare
