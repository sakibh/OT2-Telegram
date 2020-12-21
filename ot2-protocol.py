import secrets
import requests

metadata = {
    'protocolName': 'Simple Liquid Transfer',
    'author': 'Sakib <sakib.hossain@opentrons.com>',
    'description': 'Protocol with Telegram Notification',
    'apiLevel': '2.8'
}

def run(ctx):

    token = "Bot Token Here"
    bot_chatIDs = ["Chat ID Here"]

    def sendtext(bot_message):
        for chatID in bot_chatIDs:
            http_req = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chatID + '&parse_mode=Markdown&text=' + bot_message
            response = requests.get(http_req)

    # Load labware
    deep_well_plate = ctx.load_labware('nest_96_wellplate_2ml_deep', 3)
    tuberack = ctx.load_labware('opentrons_6_tuberack_falcon_50ml_conical', 4)
    tiprack = ctx.load_labware('opentrons_96_tiprack_300ul', 6)

    # Load pip
    p300 = ctx.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack])

    # Get first 10 wells
    sample_wells = deep_well_plate.wells()[:10]

    # Reagent
    reagent = tuberack['A1']

    # Transfer
    p300.transfer(100, reagent, sample_wells)

    sendtext("Protocol Complete!")