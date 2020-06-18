def split_layers_to_3(im):
    return [im[:,:, channel] for channel in range(3)] 

def avg_image(im):
    lay1, lay2, lay3 = split_layers_to_3(im)
    avgd = (1./3.)*lay1 + (1./3.)*lay2 + (1./3.)*lay3

    return avgd.astype(int)