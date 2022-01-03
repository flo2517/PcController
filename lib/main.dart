
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(title: 'Controleur de pc', home: Remote());
  }
}

class Remote extends StatelessWidget {
  const Remote({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Pc controller'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            SizedBox(
              height: 100,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: <Widget>[
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.volume_off_rounded),
                      onPressed: () {},
                    ),
                  ),
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.volume_down_rounded),
                      onPressed: () {},
                    ),
                  ),
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.volume_up_rounded),
                      onPressed: () {},
                    ),
                  ),
                ],
              ),
            ), //Controle du volume
            SizedBox(
              height: 100,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.play_circle_outline_rounded),
                      onPressed: () {},
                    ),
                  ),
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.pause_circle_outline_rounded),
                      onPressed: () {},
                    ),
                  ),
                ],
              ),
            ), //play pause
            SizedBox(
              height: 100,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.lock_outline_rounded),
                      onPressed: () {},
                    ),
                  ),
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.power_settings_new_rounded),
                      onPressed: () {
                        showDialog(
                            context: context,
                            barrierDismissible: false,

                            builder: (_) =>
                                CupertinoAlertDialog(
                                  title: Text("clique"),
                                  //content: Text("fezgzge"),
                                  actions:
                                    <Widget>[
                                      CupertinoDialogAction(
                                        child: Text('ok'),
                                        onPressed: () {
                                          Navigator.of(context).pop();
                                        },
                                      ),

                                    ],

                                )
                        );

                      },
                    ),
                  ),
                ],
              ),
            )//
          ],
        ),
      ),
    );
  }
}
