import 'package:flutter/material.dart';
import 'package:spotify/core/config/theme/app_theme.dart';

import 'presentation/splash/pages/splash.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Spotify',
      theme: AppTheme.lightTheme,
      home: const SplashScreen(),
    );
  }
}
