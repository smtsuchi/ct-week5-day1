from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def hello_world():
    context = {
        'title': "Shoha's Top 5 | Home",
        'category': 'Select a category',
        'home_button': ''
    }
    return render_template('index.html', **context)

@app.route('/musical_artists')
def getMusicalArtists():
    context = {
        'title': "Shoha's Top 5 | Musical Artists",
        'category': "Musical Artists",
        'home_button': 'Return Home',
        'cards': [
            {
                'name': 'Bruno Mars',
                'class': 'ma-card1'
            },
            {
                'name': 'Luke Christopher',
                'class': 'ma-card2'

            },
            {
                'name': 'JID',
                'class': 'ma-card3'
            },
            {
                'name': 'Saba',
                'class': 'ma-card4'
            },
            {
                'name': 'Mac Miller',
                'class': 'ma-card5'
            }
        ]
    }
    return render_template('ma.html', **context)

@app.route('/foods')
def getFoods():
    context = {
        'title': "Shoha's Top 5 | Foods",
        'category': "Foods",
        'home_button': 'Return Home',
        'cards': [
            {
                'name': 'Sushi',
                'class': 'f-card1'
            },
            {
                'name': 'Tacos',
                'class': 'f-card2'

            },
            {
                'name': 'Pad See Ew',
                'class': 'f-card3'
            },
            {
                'name': 'Tonkotsu Ramen',
                'class': 'f-card4'
            },
            {
                'name': 'Beef Bulgogi',
                'class': 'f-card5'
            }
        ]
    }
    return render_template('foods.html', **context)

@app.route('/places_visited')
def getPlacesVisited():
    context = {
        'title': "Shoha's Top 5 | Places Visited",
        'category': "Places Visited",
        'home_button': 'Return Home',
        'cards': [
            {
                'name': 'Havana, Cuba',
                'class': 'pv-card1'
            },
            {
                'name': 'Cape Town, South Africa',
                'class': 'pv-card2'

            },
            {
                'name': 'Anchorage, Alaska',
                'class': 'pv-card3'
            },
            {
                'name': 'Shibuya, Japan',
                'class': 'pv-card4'
            },
            {
                'name': 'Seoul, South Korea',
                'class': 'pv-card5'
            }
        ]
    }
    return render_template('pv.html', **context)

@app.route('/board_games')
def getBoardGames():
    context = {
        'title': "Shoha's Top 5 | Board Games",
        'category': "Board Games",
        'home_button': 'Return Home',
        'cards': [
            {
                'name': 'Dixit',
                'class': 'bg-card1'
            },
            {
                'name': '7 Wonders',
                'class': 'bg-card2'

            },
            {
                'name': 'Mouse Trap',
                'class': 'bg-card3'
            },
            {
                'name': 'Scotland Yard',
                'class': 'bg-card4'
            },
            {
                'name': 'Ticket to Ride',
                'class': 'bg-card5'
            }
        ]
    }
    return render_template('bg.html', **context)

@app.route('/sports_figures')
def getSportsFigures():
    context = {
        'title': "Shoha's Top 5 | Sports Figures",
        'category': "Sports Figures",
        'home_button': 'Return Home',
        'cards': [
            {
                'name': 'Kobe Bryant',
                'class': 'sf-card1'
            },
            {
                'name': 'Lionel Messi',
                'class': 'sf-card2'

            },
            {
                'name': 'Ichiro Suzuki',
                'class': 'sf-card3'
            },
            {
                'name': 'Michael Jordan',
                'class': 'sf-card4'
            },
            {
                'name': 'Ronaldinho de Assis Moreira',
                'class': 'sf-card5'
            }
        ]
    }
    return render_template('sf.html', **context)