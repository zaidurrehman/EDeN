import os


def test_notebooks():
    notebooks = ['Nearest_Neighbors_and_Gram_Matrix.ipynb']
    for notebook in notebooks:
        cmd = 'wget -q https://raw.githubusercontent.com/fabriziocosta/EDeN_examples/master/%s' % notebook
        os.system(cmd)
        cmd = 'jupyter nbconvert  --stdout --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 %s > /dev/null' % notebook
        res = os.system(cmd)
        os.system('rm -f %s' % notebook)
        #os.system('rm -f %s' % notebook[:])
        assert res == 0

def test_notebooks2():
    notebook = 'cascade.ipynb'
    cmd = 'wget -q https://raw.githubusercontent.com/smautner/GraphLearn_examples/master/notebooks/%s'  % notebook
    os.system(cmd)
    cmd = 'jupyter nbconvert  --stdout --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=300 %s > /dev/null' % notebook
    res = os.system(cmd)
    os.system('rm -f %s' % notebook)
    assert res == 0


