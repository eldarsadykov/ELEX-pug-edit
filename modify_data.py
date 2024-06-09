import json
import os

os.system("clear")

with open("data.json", "r") as file:
    data = json.load(file)

    for chapter in data["chapters"]:
        chapter_index = chapter["index"] - 1
        chapter_title = chapter["title"]

        within_main_route = False

        for link_index, link_title in enumerate(chapter["links"]):

            main_route_link = False

            for route_point_index, route_point_title in enumerate(data["main_route"]):
                if route_point_index < len(data["main_route"]) - 1:
                    origin = data["main_route"][route_point_index]
                    destination = data["main_route"][route_point_index + 1]
                    if (origin == chapter_title) & (destination == link_title):
                        main_route_link = True
                        within_main_route = True
                        break

            data["chapters"][chapter_index]["links"][link_index] = {
                "target": link_title,
                "main_route_link": main_route_link,
            }
        data["chapters"][chapter_index]["within_main_route"] = within_main_route

with open("data_2.json", "w") as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))