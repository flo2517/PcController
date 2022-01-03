import 'package:flutter/material.dart';
import 'package:flutter_app/pages/login_page.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: "login",
        home : login()
    );
  }
}
