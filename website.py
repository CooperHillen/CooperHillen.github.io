from flask import*

app = Flask(__name__)

#Dictionary for jokes
fav_joke = []

fav_chits = []

fav_pics = []

#This is the Main page where the jokes will be posted by users

@app.route('/')
def index():
    print(session)
    if 'username' not in session:
        return redirect('/login')
    username = session['username']
    return render_template('website.html', fav_joke=fav_joke)

#this will save the joke + username +(soon) votes for them the be
#seen on the ('/') page

@app.route('/save_joke', methods=['POST'])
def save_food():
    user_fav_joke = {'message':request.form.get('fav_joke'),
                    'end':request.form.get('end_joke'),
                    'username': session['username']}

    fav_joke.append(user_fav_joke)

    return redirect('/')

#This runs the login page

@app.route('/login')
def login():
    return render_template('login.html')

#This makes sure that the user has a session and their jokes
#will be posted with their username

@app.route('/login', methods=['POST'])
def login_post():
    session['username'] = request.form.get('username')
    return redirect('/')

urls = []

#This page is fro sharing funny url links for pictures
#will be posted with their username
@app.route('/picturesharing')
def ps():
    print(session)
    if 'username' not in session:
        return redirect('/login')

    return render_template('sharing.html', fav_pics=fav_pics)

#this saves the links for the url and allows
#it to be post on the /picturesharing
@app.route('/save_chat', methods=['POST'])
def save_chat():
    user_fav_pic_dict = {'username': session['username'],
                         'url': request.form.get('url')}
    fav_pics.append(user_fav_pic_dict)

    return redirect('/picturesharing')

#this page is for a chat room
#the messages will be post with a username
@app.route('/chat_room')
def chat_room():
    if 'username' not in session:
        return redirect('/login')
    username = session['username']
    return render_template('chatroom.html', fav_chits=fav_chits)

#This page saves the message and allows
#the message to be posted on the /chat_room
@app.route('/save_chit', methods=['POST'])
def save_chit():
    user_fav_chit_dict = {
        'username' : session['username'],
        'message' : request.form.get('fav_chit')
    }
    fav_chits.append(user_fav_chit_dict)

    return redirect('/chat_room')


app.secret_key = 'ugwefcuyg3ch348yg87cgr8c9g'
app.run(debug=True)
