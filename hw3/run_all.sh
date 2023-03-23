apt install python-pip
pip install tabulate

mkdir test0
cp tcas0.c test0
cp tests.csv test0
cp fl_dstar.py test0
cd test0 || return
.././run_tests.sh 0
python fl_dstar.py ./pdir ./fdir
cd ..

mkdir test1
cp tcas1.c test1
cp tests.csv test1
cp fl_dstar.py test1
cd test1 || return
.././run_tests.sh 1
python fl_dstar.py ./pdir ./fdir
cd ..

mkdir test3
cp tcas3.c test3
cp tests.csv test3
cp fl_dstar.py test3
cd test3 || return
.././run_tests.sh 3
python fl_dstar.py ./pdir ./fdir
cd ..

mkdir test4
cp tcas4.c test4
cp tests.csv test4
cp fl_dstar.py test4
cd test4 || return
.././run_tests.sh 4
python fl_dstar.py ./pdir ./fdir
cd ..