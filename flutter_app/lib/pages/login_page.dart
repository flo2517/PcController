// ignore_for_file: prefer_const_literals_to_create_immutables, prefer_const_constructors

import 'dart:developer';


import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_app/pages/control_page.dart';
import 'package:flutter_app/pages/sign_in.dart';
import 'package:http/http.dart';

class login extends StatefulWidget {
  const login({Key? key}) : super(key: key);

  @override
  _loginState createState() => _loginState();
}

class _loginState extends State<login> {
  final url ="http://192.168.149.35:8080/login";
  bool hidePassword = true;
  bool isRememberMe = false;
  TextEditingController _emailCo = TextEditingController();
  TextEditingController _pswdCo = TextEditingController();

  void loginRequest() async{
    var response = await post(Uri.parse(url),body: {
      "email" : _emailCo.text,
      "password" : _pswdCo.text
    });
    log(response.body);

    print(response.body);
  }

  Widget buildEmail (){
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          'Email',
          style:TextStyle(
              color: Colors.white,
              fontSize: 16,
              fontWeight: FontWeight.bold
          ),
        ),
        SizedBox(height: 10),
        Container(
          alignment: Alignment.centerLeft,
          decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
              boxShadow: [
                BoxShadow(
                    color: Colors.black26,
                    blurRadius: 6,
                    offset: Offset(0,2)
                )
              ]
          ),
          height: 60,
          child: TextField(
            controller: _emailCo,
            keyboardType: TextInputType.emailAddress,
            style: TextStyle(
                color: Colors.black87
            ),
            decoration: InputDecoration(
                border: InputBorder.none,
                contentPadding: EdgeInsets.only(top: 14),
                prefixIcon: Icon(
                    Icons.email,
                    color: Colors.blue
                ),
                hintText: 'Email',
                hintStyle: TextStyle(
                    color: Colors.black26

                )
            ),
          ),
        )
      ],
    );
  }
  Widget buildPassword (){
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          'Mot de passe',
          style:TextStyle(
              color: Colors.white,
              fontSize: 16,
              fontWeight: FontWeight.bold
          ),
        ),
        SizedBox(height: 10),
        Container(
          alignment: Alignment.centerLeft,
          decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
              boxShadow: [
                BoxShadow(
                    color: Colors.black26,
                    blurRadius: 6,
                    offset: Offset(0,2)
                )
              ]
          ),
          height: 60,
          child: TextField(
            controller: _pswdCo,
            obscureText: hidePassword,
            style: TextStyle(
                color: Colors.black87
            ),
            decoration: InputDecoration(
                border: InputBorder.none,
                contentPadding: EdgeInsets.only(top: 14),
                prefixIcon: Icon(
                    Icons.lock,
                    color: Colors.blue
                ),
                suffixIcon: IconButton(
                  onPressed: () {
                    setState(() {
                      hidePassword = !hidePassword;
                    });
                  },
                  color:  Colors.blue,
                  icon: Icon(hidePassword
                      ? Icons.visibility_off
                      : Icons.visibility),
                ),


                hintText: 'Mot de passe',
                hintStyle: TextStyle(
                    color: Colors.black26

                )
            ),
          ),
        )
      ],
    );
  }

  Widget buildForgotPassBtn(){
    return Container(
      alignment: Alignment.centerRight,
      child: FlatButton(
        onPressed:( ) =>{

        },
        padding: EdgeInsets.only(right: 0),
        child: Text(
          'Mot de passe oublié ?',
          style: TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.bold
          ),
        ),
      ),
    );
  }

  Widget buildRemember (){
    return Container(
      height: 20,
      child: Row(
        children: <Widget> [
          Theme(
              data: ThemeData(unselectedWidgetColor: Colors.white),
              child: Checkbox (
                value: isRememberMe,
                checkColor: Colors.blue,
                activeColor: Colors.white,
                onChanged: (value){
                  setState(() {
                    isRememberMe = value!;
                  });
                },
              )),
          Text(
            'Se souvenir de moi',
            style: TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.bold,
            ),
          )
        ],
      ),
    );
  }
  Widget buildLoginBtn(){
    return Container(
      padding: EdgeInsets.symmetric(vertical: 25),
      width: double.infinity,
      child: RaisedButton(
        elevation: 5,
        onPressed: ()=> {
          // Navigator.of(context).(MaterialPageRoute(
          //     builder: (context)=>Remote()
          // ))
          print(_emailCo.text+" "+_pswdCo.text),
          loginRequest(),
          Navigator.push(context, MaterialPageRoute(builder: (context)=> Remote()))
        } ,
        padding: EdgeInsets.all(15),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(15)
        ),
          color: Colors.white,
        child: Text(
          'Se connecter',
          style: TextStyle(
            color : Colors.blue,
            fontSize: 18,
            fontWeight: FontWeight.bold
          ),
        ) ,
      ),
    );
  }
Widget buildSignupBtn(){
      return GestureDetector(
        onTap: ()=> {
          Navigator.push(context, MaterialPageRoute(builder: (context)=> signIn()))
        },
        child: RichText(
          text : TextSpan (
            children: [
              TextSpan(
                text: "Pas de compte ? ",
                style : TextStyle(
                  color : Colors.white,
                  fontSize: 18,
                  fontWeight: FontWeight.w500

                )
              ),
              TextSpan(
                text: 'S\'inscrire',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 18,
                  fontWeight: FontWeight.bold
                )
              )
            ]
          )
        ),
      );
}

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: AnnotatedRegion<SystemUiOverlayStyle>(
        value: SystemUiOverlayStyle.light,
        child: GestureDetector(
          child: Stack(
            children: <Widget>[
              Container(
                height: double.infinity,
                width: double.infinity,
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [
                      Colors.blue,
                      Colors.blue[300]!,
                      Colors.blue[100]!,

                    ]
                  )
                ),
               child: SingleChildScrollView(

                 padding: EdgeInsets.symmetric(
                   horizontal: 25,
                   vertical: 120
                 ),
                 child: Column(
                   mainAxisAlignment: MainAxisAlignment.center,
                   children: <Widget>[
                     Text(
                       "Se connecter",
                       style : TextStyle(
                           color : Colors.white,
                           fontSize: 40,
                           fontWeight: FontWeight.bold
                       ),
                     ),
                     SizedBox(height: 50),
                     buildEmail(),
                     SizedBox(height: 20),

                     buildPassword(),
                     buildForgotPassBtn(),
                     buildRemember(),
                     buildLoginBtn(),
                     buildSignupBtn()
                   ],
                 ),
               ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
