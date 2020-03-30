# Information for Annotators

## Getting Started

First, thank you for helping us with the annotation. Our fate is somewhat in your hands now (and vice versa). Go team!

### First time using MAE:

Click on ```MAE_2.2.10.jar``` in the root directory. You might get a warning dialog, if you are using Mac,
control-click ```MAE_2.2.10.jar```, then choose `Open` from the shortcut menu. Then, click `Open`.

1. `File`→`New Task Definition`
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/1_definition.png" width="70%" height="70%">

2. Choose the `TempRelTask.dtd`, click `Open`
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/2_dtd.png" width="70%" height="70%">

3. Click the `EVENT_ORDER` and tick the box
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/3_order.png" width="70%" height="70%">

4. `File` →`Open Document`, then open the file assigned to you. 
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/4_openxml.png" width="70%" height="70%">

5. click `Yes`
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/5_xml.png" width="70%" height="70%">

6. Begin your annotation journey!
<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/6_relation.png" width="70%" height="70%">

## Annotation Schema and Guildeline
See our regularly updated [guildeline](https://docs.google.com/document/d/1LZXOLTrth4FPP0_m9PauW0k9P-En9mYyvY4qOHSPs2I/edit?usp=sharing)


### How to delete:
Choose the row you want to delete, control-click, then choose `Delete <id>-(fromID, toID)` from the shortcut menu, click it to delete the relation. (Please take note of which verb pair, which article and which paragraph of the article you delete in a txt file.)

<img src="https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files/blob/master/img/problems/delete_aux.png" width="70%" height="70%">

### How to use git for this task:

- Clone to local:
```
$ git clone https://github.com/YonglinWang-Brandeis/cs140-groupB-annotation-files.git
```
- 【Annotate your task】

- Once you have done your part, commit and push it with TAG.

  a. Check which file you have modified and want to stage for commit:
    ```
    $ git status
    ```
  b. Update what will be committed using `$ git add`:
    ```
    $ git add .
    ```
  c. Commit and push, here we use `annotator1` as an example:
    ```
    $ git commit -m ‘update by annotator1’
    $ git push
    ```
  d. Create a Annotated Tag using `$ git tag -a <tag name> -m "message"`:
    ```
    $ git tag -a phase1_annotator1 -m "phase1 annotator1"
    ```  
  e. Push the tag to server using `$ git push origin <tag>`: 
    ```
    $ git push origin phase1_annotator1
    ```

CAVEAT: Tags are not mutable, and you cannot make a change under an existing TAG, you have to delete and recreate your TAG:

\_d. Delete and recreate the tag:
```
$ git tag -d phase1_annotator1
$ git tag -a phase1_annotator1 -m "phase1 annotator1"
```
\_e. Delete the old tag from the server and push the new tag to the server:
```
$ git push origin :phase1_annotator1
$ git push origin phase1_annotator1
```

For more inforation, please check the [official guide](https://git-scm.com/book/en/v2/Git-Basics-Tagging). Or contact with Group B members.





