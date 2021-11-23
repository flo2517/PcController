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
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: <Widget>[
                Transform.scale(
                  scale: 2,
                  child: Container(
                    color: Colors.purpleAccent,
                    child: IconButton(
                      icon: const Icon(Icons.volume_off_rounded),
                      onPressed: () {},
                    ),
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
            )
          ],
        ),
      ),
    );
  }
}
