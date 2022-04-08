from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Computer
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        new_computer = request.form.get('computer')
        new_computer_ip = request.form.get('computer_ip')

        old_computer_ip = Computer.query.filter_by(computer_ip=new_computer_ip).first()

        if old_computer_ip:
            flash(old_computer_ip.data + ' already has this IP address', category='error')
        elif len(new_computer) < 1:
            flash('Name is too short!', category='error')
        else:
            new_computer = Computer(data=new_computer, computer_ip=new_computer_ip, user_id=current_user.id)
            db.session.add(new_computer)
            db.session.commit()
            flash('Computer added!', category='success')

    computerList = Computer.query.all()
    return render_template("home.html", user=current_user, computerList=computerList)


@views.route('/delete-computer', methods=['POST'])
def delete_computer():
    computer = json.loads(request.data)
    computerId = computer['computerId']
    computer = Computer.query.get(computerId)
    if computer:
        if computer.user_id == current_user.id:
            db.session.delete(computer)
            db.session.commit()

    return jsonify({})

@views.route('/patch-computer', methods=['POST'])
def patch_computer():
    computer = json.loads(request.data)
    computerId = computer['computerId']
    computer = Computer.query.get(computerId)
    if computer:
        if computer.user_id == current_user.id:
            db.session.delete(computer)
            db.session.commit()

    return jsonify({})
