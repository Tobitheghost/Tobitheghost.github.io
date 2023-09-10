from flask import Blueprint, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from .utils import mailUsername
from website import mail
from .data import data, land_use_code, movieData


homePage = Blueprint('homePage', __name__)

@homePage.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        contact_msg = request.form.get('contact_msg')
        msg = Message(subject=f"ContactWebpage: {name} at {email}", body=contact_msg, recipients=[mailUsername], sender=email)
        mail.send(msg)
        msg2 = Message(subject=f"Thank You for Contacting Me!", body="Thank you for getting in contact with me. I will read your message asap!", recipients=[email], sender=mailUsername)
        mail.send(msg2)
        return render_template("index.html", success=True)
    return render_template("index.html")

@homePage.route("/movies")
def movies():
    listoftitles = movieData['title'].values
    listofdates = movieData['release date'].values
    listofdesc = movieData['gen desc'].values
    listofyoutube = movieData['youtube'].values
    listofposter = movieData['poster'].values
    count = len(listoftitles)
    return render_template("movies.html", titles = listoftitles, dates = listofdates, desc = listofdesc, youtube = listofyoutube, posters = listofposter, count=count)

@homePage.route("/TexasToms")
def texas():
    return render_template('texas toms.html')

@homePage.route("/games")
def games():
    return render_template('games.html')

@homePage.route("/tictactoe")
def tictactoe():
    return render_template('tictactoe.html')

@homePage.route('/maps')
def maps():
    return render_template('maps.html')

@homePage.route('/search')
def search():
    q = request.args.get('q')
    if q:
        res = data[data['ADDRESS'].str.lower().astype(str).str.startswith(str(q))][['ADDRESS']].head(50)
        ind = data[data['ADDRESS'].str.lower().astype(str).str.startswith(str(q))][['OBJECTID']].head(50)
        loc = data[data['ADDRESS'].str.lower().astype(str).str.startswith(str(q))][['the_geom']].head(50)

        loc = loc.values
        res = res.values
        ind = ind.values

        result_content = []
        loc_content = []
        index_content = []
        for x in range(len(res)):
            parcelpolygon = []
            multipolygon = loc[x]
            multipolygon = multipolygon[0]
            multipolygon = multipolygon.split('(((')[1]
            multipolygon = multipolygon.split(')))')[0]
            multipolygon = multipolygon.split(',')
            for item in multipolygon:
                item = item.replace(" -", "-")
                y = [item.split(" ")[1], item.split(" ")[0]]
                parcelpolygon.append(y)
            combo_result = res[x]
            combo_loc = parcelpolygon
            combo_index = ind[x]
            result_content.append(combo_result)
            loc_content.append(combo_loc)
            index_content.append(combo_index)
        res = result_content
        loc = loc_content
        ind = index_content
    else:
        res = [[]]
        loc = [[]]
        ind = [[]]
    return render_template('search_results.html', results = res, location=loc, addr_index=ind)

@homePage.route('/results/<addressID>')
def results(addressID):
    q = addressID
    if q:
        def stringify(index):
            val = data[data['OBJECTID'].astype(str).str.contains(str(q))][[index]]
            value = val.values[0][0]
            if str(value) == 'nan':
                value = ''
            else:
                value = str(value)
            return value
        
        def moneyfy(index):
            valueAmt = stringify(index)
            if '.' in valueAmt:
                valueAmt = valueAmt.split('.')[0]
                if len(valueAmt)/3 > 1.0:
                    count = len(valueAmt)//3
                    for iter in range(count):
                        if (iter + 1) * 3 == len(valueAmt) - iter:
                                pass
                        else:
                            comaNumb = -1*((3 *(iter + 1)) + iter)
                            valueAmt = valueAmt[:(comaNumb)] + "," + valueAmt[(comaNumb):]
                valueAmt = (f'${valueAmt}.00')
            elif valueAmt == '0':
                valueAmt = (f'${valueAmt}.00')
            else:
                valueAmt = '0'
                valueAmt = (f'${valueAmt}.00')
            return valueAmt
        
        address = stringify('ADDRESS')
        owner = stringify('OWN_NAME')
        owner2 = stringify('OWN_NAME2')

        luc = stringify('LANDUSECODE')
        luc = str(luc)
        if '.' in luc:
            luc = luc.split('.')[0]
            land_use = land_use_code[luc]
        elif luc == '':
            land_use = ''
        else:
            land_use = luc
        
        asLandVal = moneyfy('ASSESSED_LAND_VALUE')
        asImpVal = moneyfy('ASSESSED_IMPROVE_VALUE')
        ExLandVal = moneyfy('EXEMPT_LAND_VALUE')
        ExImpVal = moneyfy('EXEMPT_IMPROVE_VALUE')
        effDate = stringify('ASSESSMENT_EFFECTIVE_DATE')

        if effDate == '':
            effDate = 'Unlisted'
        if len(effDate) > 3:
            effDate = effDate.split(' ')[0]

    return render_template('parcel_results.html',parcel=q,address=address,owner=owner,owner2=owner2,land_use=land_use,asLandVal=asLandVal,asImpVal=asImpVal,ExLandVal=ExLandVal,ExImpVal=ExImpVal,effDate=effDate) 
