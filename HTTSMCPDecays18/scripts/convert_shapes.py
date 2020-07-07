# you can run the combined shapes for all years using commands like the example below:
#PostFitShapesFromWorkspace -m 125 -d output/pas_2706/htt_tt_3_only_13TeV/125/combined.txt.cmb -w output/pas_2706/htt_tt_3_only_13TeV/125/ws.root -o shapes_tt_cmb_3.root --print --postfit --sampling -f output/pas_2406_v2/cmb/125/multidimfit.bestfit.root:fit_mdf --total-shapes-bin=true --total-shapes=true

import ROOT

fout = ROOT.TFile('shapes_ztt_cmb.root','RECREATE')

bini=3



#chans = ['mt','tt']
chans = ['mt']
bins = {'mt': [3,4,5,6,30,40,50,60], 'tt': [1,2,3,7]}

bkgs = {}

bkgs['mt'] = [
 'EmbedZTT',	
 'TTT',
 'VVT',	
 'ZL',	
 'jetFakes'
]

bkgs['tt'] = [
 'EmbedZTT',     
 'TTT',
 'VVT',  
 'ZL',   
 'jetFakes',      
 'Wfakes'      
]	

for chan in chans:
  for bini in bins[chan]:

    f = ROOT.TFile('shapes_ztt_%i.root' % bini)
    dirname = 'htt_%(chan)s_2018_%(bini)i_13TeV_postfit' % vars()
    fout.cd()
    if not ROOT.gDirectory.GetDirectory(dirname): ROOT.gDirectory.mkdir(dirname)
    
    directory = f.Get('postfit')
    for key in directory.GetListOfKeys():
      histo = directory.Get(key.GetName()).Clone()
      fout.cd(dirname)
      histo.Write()


    year_dirname = 'htt_%(chan)s_201X_%(bini)i_13TeV_postfit' % vars()
    for x in bkgs[chan]:
      h1 = f.Get(year_dirname.replace('X','6')+'/'+x).Clone()
      h2 = f.Get(year_dirname.replace('X','7')+'/'+x).Clone()
      h3 = f.Get(year_dirname.replace('X','8')+'/'+x).Clone()
      h1.Add(h2)
      h1.Add(h3)
      fout.cd(dirname)
      h1.Write()



