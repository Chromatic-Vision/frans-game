def place(block):
    # if game.player.x > TILE_SIZE * 10:
    #     game.refresh_map('test2')
    if block.type == 4:
        def update():
            if game.player.x // TILE_SIZE == block.x \
                    and game.player.y // TILE_SIZE == block.y:
                game.player.x = 2 * TILE_SIZE
                game.player.y = 2 * TILE_SIZE
                game.refresh_map('test2')

        event(Event.UPDATE, update)


event(Event.PLACE, place)
