from flask import Blueprint, render_template, redirect
import os

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/mute')
def mute():
    os.system('nircmd mutesysvolume 2')
    return redirect('/')

@views.route('volume/<volume>')
def volume(volume):
    volume = int(int(volume)*655.35)
    os.system(f'nircmd.exe setsysvolume {volume}')
    return redirect('/')