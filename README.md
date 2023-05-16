### 이차전지 공동연구
<hr>
유사한 목적의 소프트웨어 - napari 기반       
https://www.youtube.com/watch?v=Km1_TnUQ4FM
<hr>
<b> [설치 가이드] </b><br>
참고 - https://napari.org/stable/tutorials/fundamentals/installation.html
<h4> * Python package 형태로 napari install</h4>
- Prerequisites: Python 3.8 or higher / the ability to install python packages via pip or conda-forge
<pre>
<code>
conda create -y -n napari-env -c conda-forge python=3.9
conda activate napari-env
</code>
</pre>

아래의 세가지 방법 중 하나 선택하여 napari 설치
1. From pip
<pre>
<code>
python -m pip install "napari[all]"  #default framework인 PyQt5를 

# upgrade napari to a new version
python -m pip install "napari[all]" --upgrade
</code>
</pre>
2. From conda-forge
<pre>
<code>
conda install -c conda-forge napari

# upgrade napari to a new version
conda update napari

# PySide2를 backend로 사용하고 싶다면 아래 코드 실행
conda install -c conda-forge "napari=*=*pyside2"
</code>
</pre>
3. From the main branch on github
<pre>
<code>
python -m pip install "git+https://github.com/napari/napari.git#egg=napari[all]"
</code>
</pre>
 
작동하는지 확인

    napari
   
+) 추가적으로 backend framework를 PyQt5와 PySide2 중 선택하고 싶다면 아래의 코드 실행
<pre>
<code>
pip install "napari[pyqt5]"  # for PyQt5

# or
pip install "napari[pyside2]"  # for PySide2

#만약 backend를 바꾸고 싶다면, pip uninstall로 우선 삭제한 후 다른 framework 설치
</code>
</pre>

---

<h4> * bundled app 형태로 napari install</h4>
- Prerequisites: x
- https://github.com/napari/napari/releases 에서 Windows/MacOS에 맞게 다운로드


<h2> Installation </h2>
<hr>
<h3> PyPI </h3>
napari-battery is available through the Python package index and can be installed using pip.     

```
pip install napari-battery
```
<h3> Local </h3>
Also it is fine to clone this repository and install locally with

```
pip install -e . 
```
<b> napari-battery 파일 내(setup.cfg 있는 위치)에서 <code>pip install -e . </code>



     
     
     
     
     
     
     
     
     
     
     
     
     
<br> 기존 cookie cutter 만들었을 때 자동 생성되었던 README.md 내용     
     
1. `cd` into your new directory

     cd napari-battery
     #you probably want to install your new package into your env
     pip install -e .
2. Create a github repository for your plugin:
   https://github.com/new

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/your-repo-username/your-repo-name.git
     git push -u origin main

   Don't forget to add this url to setup.cfg!

     [metadata]
     url = https://github.com/your-repo-username/your-repo-name.git

4. Consider adding additional links for documentation and user support to setup.cfg
   using the project_urls key e.g.

    [metadata]
    project_urls =
        Bug Tracker = https://github.com/your-repo-username/your-repo-name/issues
        Documentation = https://github.com/your-repo-username/your-repo-name#README.md
        Source Code = https://github.com/your-repo-username/your-repo-name
        User Support = https://github.com/your-repo-username/your-repo-name/issues
5. Read the README for more info: https://github.com/napari/cookiecutter-napari-plugin

6. We've provided a template description for your plugin page at `.napari/DESCRIPTION.md`.
   You'll likely want to edit this before you publish your plugin.

7. Consider customizing the rest of your plugin metadata for display on the napari hub:
   https://github.com/chanzuckerberg/napari-hub/blob/main/docs/customizing-plugin-listing.md
