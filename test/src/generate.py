import os
import random


def generate_html(list_tuples, dataset):
    rel_app="./app/"
    current = 0
    indexing = 1
    random.seed(5344)
    random.shuffle(list_tuples)
    while current < len(list_tuples):
        if current == 0:
            nf = open(rel_app+'index.html', 'w')
        else:
            nf = open(rel_app+list_tuples[current][0], 'w')
        to_link = random.randint(3, 5)

        info = dataset[list_tuples[current][1]]
        block = info
        links = []
        c = 0
        while indexing < len(list_tuples):
            links.append((list_tuples[indexing][0], list_tuples[indexing][3]))
            c += 1
            indexing += 1
            if c == to_link:
                break
        links_html = []
        for t in links:
            s = f'<a href="./{t[0]}"> {t[1]} </a>'
            links_html.append(s)
        links_html = "<br>".join(links_html)

        my_html = f"""
        <!doctype html>
        <html>
        <head>
        <meta charset="UTF-8"/>
            <title>{list_tuples[current][3]}</title>
        </head>
        <body>
            <div>
            {
                block
            }
            <br>
             <img src="{list_tuples[current][2]}"  height="100" > 
            <br>
            </div>
            <div>
            {
                links_html
            }            
            </div>
        </body>
        </html>
        """
        my_html.encode('utf-8')
        nf.write(my_html)
        nf.close()

        current += 1


def main():
    im_folder = "./app/images/"
    relative_to_app="./images/"
    images = os.listdir(im_folder)
    uniques_images = set()
    all_names_html = []
    for name in images:

        i = len(name)-1
        while(i >= 0):
            if name[i] == '_':
                aux = name[:i]
                #print('>>>', name)
                # if aux=='Albrecht_Dürer':
                #     n= 'Albrecht_Durer'
                #     os.rename(im_folder+name,im_folder+n+name[i:])
                title = name[:name.find('.')]
                html_name = title+".html"  # file to gen
                #html_name, artistname, im_folder+name, title
                all_names_html.append((html_name, aux, relative_to_app+name, title))
                uniques_images.add(aux)
                break
            i -= 1
    #print('imx', len(images), len(all_names_html))

    # print(uniques_images)
    f = open("./artists.csv", 'r')
    classes = []
    rows = {}
    for index, line in enumerate(f):
        if index == 0:
            classes = line.strip().split(',')
        else:
            data = line.strip()

            l = data.find(',')+1
            r = data[l:].find(',')
            name = data[l:r+l]
            rows["_".join(name.split(' '))] = data[l:]
    f.close()
    generate_html(all_names_html, rows)
    # a=list(sorted(rows.keys()))
    # b=list(sorted(list(uniques_images)))
    # print('>>',a)
    # print('>>',b)
    # print('>>>', b[0]==a[0])
    # print(set(rows.keys())-uniques_images)
    # print(uniques_images-set(rows.keys()))


if __name__ == "__main__":
    main()
