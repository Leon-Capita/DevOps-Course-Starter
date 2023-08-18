


from flask import Flask, request, render_template, redirect
from ViewModelClass import ViewModel
from flask_config import Config
from data.session_items import get_items, get_item, add_item, save_item#, get_item_by_title
from logging.config import logging

app = Flask(__name__)
app.config.from_object(Config())

items = get_items()
print(f'items {items}')

