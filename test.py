from visual_genome import api
# ids = api.get_image_ids_in_range(start_index=2000, end_index=2010)
# print(ids[0])


# image = api.get_image_data(id=2001)
# print(image)

# regions = api.get_region_descriptions_of_image(id=2001)
# print(len(regions))

graph = api.get_region_graph_of_region(2001, 5553058)
print(graph.objects)


def getXY(id):
    regions = api.get_region_descriptions_of_image(id)

    for region in regions:
        print("x:", region.x, "y:", region.y)
        # pass


def getZ(id):
    pass


# getXY(2001)
