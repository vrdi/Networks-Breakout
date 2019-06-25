
@interact
def tsi_diffusion(n=input_box(default=50,label='Number of Vertices'),type=selector(['Barabasi-Albert','Erdos-Renyi','Watts-Strogatz','Configuration'],default='Erdos-Renyi',label='Graph Type',buttons=True),p=input_box(default=.2,label='Probability (ER and WS)'),k=slider([2*x for x in range(1,10)],default=2,label='k (WS)'),m=slider([1..100],default=3,label='m (BA)'),deg_seq=input_box(default=[3,3,3,3],label='Degree Sequence (Configuration)'),trials=input_box(default=100,label='Number of Trials'),ps=checkbox(True,label='Show graph?'),pd=checkbox(True,label='Plot degrees?'),scalex=checkbox(True,label='Scale x-axis?'),auto_update=False):
    
    
   
    dens=0
    avg_deg=0
    trans=0
    diam=0
    avg_dist=0
    temp=[]
    temph=[]
    for i in range(n):
        temp.append(0)
    for i in range(trials):
        #initialization
        if type=='Erdos-Renyi':
            g=graphs.RandomGNP(n,p)
        if type=='Barabasi-Albert':
            g=graphs.RandomBarabasiAlbert(n,m)
        if type=='Watts-Strogatz':
            g=graphs.RandomNewmanWattsStrogatz(n,k,p)
        if type=='Configuration':
            h=graphs.DegreeSequenceConfigurationModel(deg_seq)
            h.remove_multiple_edges()
            h.remove_loops()
            g=h.to_simple(to_undirected=True)
            g.edges(labels=False)
        
        dens=dens+g.density()
        avg_deg=avg_deg+g.average_degree()
        trans=trans+g.cluster_transitivity()
        diam=diam+g.diameter()
        avg_dist=avg_dist+g.average_distance()
        gvec=g.degree_histogram()
        for j in range(len(gvec)):
            temp[j]+=gvec[j]
        gvec=g.degree()
        for j in range(len(gvec)):
            temph.append(gvec[j])
	
	
            

    pretty_print('Density: ',(dens/trials).n())
    pretty_print('Average Degree: ',(avg_deg/trials).n())
    pretty_print('Transitivity: ',(trans/trials))
    pretty_print('Diameter: ',(diam/trials).n())
    pretty_print('Average Path Length: ', (avg_dist/trials).n())
        
            
            

        
    if ps==True:
        g.show()
    if pd==True:
        
        if scalex==True:
        
            count0=0
        
            for i in range(len(temp)):
                if temp[i]!=0:
                    count0=0
                else:
                    count0+=1
                
            for i in range(count0):
                temp.pop()
            
            for i in range(5):
                temp.append(0)
            
        temp_p=list_plot(temp,size=40)#(g.degree_histogram(),size=40)
        
        temp_p.axes_labels(['Degree', 'Frequency'])
        temp_p.show(title="Aggregate Degree Frequencies")
        from sage.plot.histogram import Histogram

        h=histogram(temph)#,bins=len(temp)-5)
        h.axes_labels(['Degree', 'Frequency'])
        h.show(title="Histogram Degree Frequencies")



