import 'dart:developer';
//import 'dart:math';
import 'package:flutter/material.dart';
 showAlertDialog(BuildContext context, String text, String title, {bool sign  = false, bool rename = false}) {

  // set up the button
  Widget okButton = TextButton(
    child: Text("OK"),
    onPressed: () {
      Navigator.of(context).pop(); // dismiss dialog
      if(sign){
        Navigator.of(context).pop();
      }
      if(rename){
        Navigator.of(context).pop();
      }
    },
  );

  // set up the AlertDialog
  AlertDialog alert = AlertDialog(
    title: Text(title),
    content: Text(text),
    actions: [
      okButton,
    ],
  );

  // show the dialog
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return alert;
    },
  );
}

class EmailValidator {


  static bool Validate (String value, BuildContext context){
    if(value.isEmpty){
      showAlertDialog(context , "The mail must not me empty","Email input");
      return false;

    }
    RegExp regExp = RegExp(
      r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$',
      caseSensitive: false,
      //multiLine: false,
    );
    log(value);
    if(!regExp.hasMatch(value)){
      showAlertDialog(context , "The format of the email address isn't correct","Email input");

      return false;
    }

    return true;
  }
}
class PasswordValidator {
  static bool Validate (String value, BuildContext context){
    if(value.isEmpty){
      showAlertDialog(context , "The password must not be empty","Password input");
      return false;

    }
    if(value.length <8){
      showAlertDialog(context , "The password must have at least 8 character","Password input");
      return false;
    }
    RegExp regExp = RegExp(
      r'^(?=.[a-z])(?=.[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$',
      caseSensitive: false,
      //multiLine: false,
    );
    log(value);
    if(!regExp.hasMatch(value)){
      showAlertDialog(context , "The format of the password isn't correct\n8 character,1 maj, 1min,1 special minimum ","Password input");

      return false;
    }

    return true;
  }
}

