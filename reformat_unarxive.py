import tarfile, os, shutil
from tqdm import tqdm
from covid19_gpt2.convenience_functions.utils import download_url, small_version, ProgressFileObject

CDIR = os.path.dirname(os.path.realpath(__file__))
DATADIR = os.path.join(CDIR, 'data')

url = 'https://zenodo.org/record/3385851/files/unarXive.tar.bz2?download=1'
tarpath = os.path.join(DATADIR, 'unarXive.tar.bz2')
UNATXT = os.path.join(DATADIR, 'unarxive.txt')
UNASMALLTXT = os.path.join(DATADIR, 'unarxive_small.txt')

if not False: # os.path.isfile(UNATXT):
    try:
        os.mkdir(DATADIR)
    except:
        pass

    if not os.path.isfile(tarpath):
        try:
            download_url(url, tarpath)
        except Exception as e:
            print(e)

    try:
        pfo = ProgressFileObject(tarpath)
        tar = tarfile.open(fileobj=pfo)
        print(tar.getmembers())
        #tar.extractall('data')
        tar.close()
        pfo.close()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)

    """
    articles = os.listdir(r'data/unarXive/papers')
    articles = sorted([article for article in articles if article[:2] in ['20', '19', '18', '17']])  # ]])

    # ['<|endoftext|>']
    with open(UNATXT, 'w', encoding='cp850', errors='replace') as f_write:
        for article in tqdm(articles):
            with open(r'data/unarXive/papers/' + article, 'r', encoding='cp850', errors='replace') as f_read:
                for line in f_read:
                    f_write.write(line)
                f_write.write('<|endoftext|>')


    with open(UNASMALLTXT, 'w', encoding='cp850', errors='replace') as f_write:
        for article in tqdm(articles[:2]):
            with open(r'data/unarXive/papers/' + article, 'r', encoding='cp850', errors='replace') as f_read:
                for line in f_read:
                    f_write.write(line)
                f_write.write('<|endoftext|>')

    shutil.rmtree(r'data/unarXive/', ignore_errors=True)
    #os.remove('data/unarXive.tar.bz2')
    """


