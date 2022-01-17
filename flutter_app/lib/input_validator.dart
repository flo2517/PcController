import 'package:flutter/material.dart';

class EmailValidator {

  static String? Validate (String value){
    if(value.isEmpty){
      return "Le mail ne doit pas être vide";
    }

    return null;
  }
}

