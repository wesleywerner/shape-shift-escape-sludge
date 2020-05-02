# Technical Details

## Warping to a new room

A call to `uiWarp (room);`. This clears the current room and stores ego's position, which gets flipped on the X-axiz so that you can use variables `egoExitX` and `egoExitY` in the new room to position ego near where you exited.

## Setting up a room

Add regions to trigger room warping:

    `addRoomExits(leftExitRoomPtr, rightExitRoomPtr)`

## Add a new Inventory item

Create the objectType (preferably in inventory.slu) with these events:

    getIcon:
        set the global `icon` variable for the inventory item
        `icon = anim('data/inventory.duc', 0);`

    takeIt:
        Shows the take-hand cursor and is called when the player takes the item.
        call `moveCharacter` and `giveInventory(yourItemObjectHere);`
    
## Use an inventory item

Create an event on the object to use the inventory item.

    objectType myItem("foo") {
        event bar {
            # bar interacts with foo
            }
        }

## Generate a walkable floor map from a PNG

Draw a floor map where black indicates unwalkable areas and any other color indicates walkable. 

Then run `python floor-gen.py -i data/imagefile.png`

The result is saved to `data/imagefile.flo`, a Sludge floor plan file.
