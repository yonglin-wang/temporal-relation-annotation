# Information for Grader

Hello! This is Group B and welcome to our GitHub Repository. 

You can find the required submissions by clicking on the following links:

- [Final written report](/submissions/GroupB_FinalProjectWriteUp_COSI140B.pdf)
- [Final presentation slides](/submissions/COSI140B.GroupB.FinalAnnotationProjectPresentation.pdf)
- [The Gold Standard Corpus](/code/data/gold_standard.csv) and [features extracted from the Gold Standard](/code/features_gold.csv)

- [A folder of code for the machine learning models](/code/models/)

----

# Information for Annotators

## Getting Started

First, thank you for helping us with the annotation. Our fate is somewhat in your hands now (and vice versa). Go team!

### How to use git for this task:

- Fork this repo. 
  So you can have a personal copy. You can do anything to the copy without affecting the original one. 
  <img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/forkrepo.jpg" width="40%" height="40%">

- Navigate to your copy of the repository and click the green "Clone or download" button. Click the clipboard next to the https clone URL to copy it.
  ```
  $ git clone <paste the URL here>
  ```
- 【Annotate your task】

- Create a new branch. `git checkout -b <branch name>`
  ```
  git checkout -b phase1-Annotator1
  ```
- add, commit and push the new branch.
  ```
  git add <your annotated tasks>
  git commit -m "<messages you wanna add>"
  git push -u origin <branch name>
  ```
  **CAVEATE**: only make changes to the file with the number you were allocated, otherwise your request may be rejected!
  
- Navigate to the original GitHub repository, and you should see a big green button marked "Compare and pull request". Click that button and you will be taken to a page giving you the opportunity to describe your pull request and showing you the changes you have made:

  <img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/open_pull.jpg" width="70%" height="70%">

  Then, click the big green button `Create pull request`. 
  Done!


For more information, please check the [official website](https://archaeogeek.github.io/gettingstartedwithgit/github/pullrequest.html).

### First time using MAE:

Click on ```MAE_2.2.10.jar``` in the root directory. (You might get a warning dialog, if you are using Mac.
Control-click ```MAE_2.2.10.jar```, then choose `Open` from the shortcut menu. Then, click `Open`.)

1. Choose `File`→`New Task Definition`:
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/1_definition.png" width="70%" height="70%">

2. Choose the `TempRelTask.dtd`, click `Open`:
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/2_dtd.png" width="70%" height="70%">

3. Click the `EVENT_ORDER` and tick the box:
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/3_order.png" width="70%" height="70%">

4. Choose `File` →`Open Document`, then open the file assigned to you:
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/4_openxml.png" width="70%" height="70%">

5. click `Yes`:
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/5_xml.png" width="70%" height="70%">

6. Begin your annotation journey!
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/6_relation.png" width="70%" height="70%">

## Annotation Schema and Guildeline
See our regularly updated [guildeline](https://docs.google.com/document/d/1LZXOLTrth4FPP0_m9PauW0k9P-En9mYyvY4qOHSPs2I/edit?usp=sharing)


### How to delete:
- Choose the word you want to delete, and you will see all the relations are highlighted automatically:
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/problems/delete_not_verb.png" width="70%" height="70%">

- Control-click, then choose `Delete <id> (word)` from the shortcut menu:
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/problems/delete_not_verb_1.png" width="70%" height="70%">

- Click `OK` to delete all the links connected to the word:
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/problems/delete_not_verb_2.png" width="70%" height="70%">

- You did it! (Please take note of which verb, which article and which paragraph of the article you delete in your txt file.)
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/problems/delete_not_verb_3.png" width="70%" height="70%">
