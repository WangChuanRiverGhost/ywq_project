import pdb;

my_pdb = pdb.Pdb(skip=["第三方库.*"], colorize=True,backend="monitoring") 
my_pdb.set_trace()

try:
    x = 1/0
except Exception as e:
    pass
    pdb.post_mortem(e)

