import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_svg/svg.dart';
import 'package:spotify/common/widgets/buttons/main_button.dart';
import 'package:spotify/common/widgets/buttons/mode_selection_button.dart';
import 'package:spotify/core/config/assets/app_images.dart';
import 'package:spotify/core/config/assets/app_vectors.dart';
import 'package:spotify/presentation/auth/pages/auth_select.dart';
import 'package:spotify/presentation/mode/bloc/theme_cubit.dart';

class ModeSelection extends StatelessWidget {
  const ModeSelection({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          Container(
            decoration: const BoxDecoration(
              image: DecorationImage(
                  fit: BoxFit.fill, image: AssetImage(AppImages.modeScreen)),
            ),
          ),
          Container(
            color: Colors.black.withOpacity(0.12),
          ),
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.symmetric(
                horizontal: 24,
                vertical: 8,
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Align(
                      alignment: Alignment.topCenter,
                      child: SvgPicture.asset(AppVectors.logo)),
                  const Spacer(),
                  const Text(
                    textAlign: TextAlign.center,
                    'Choose Mode',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                      fontSize: 28,
                    ),
                  ),
                  const SizedBox(
                    height: 24,
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      ModeSelectionButton(
                        onTap: () {
                          context
                              .read<ThemeCubit>()
                              .updateTheme(ThemeMode.light);
                        },
                        icon: AppVectors.lightIcon,
                        modeName: 'Light Mode',
                      ),
                      ModeSelectionButton(
                        onTap: () {
                          context
                              .read<ThemeCubit>()
                              .updateTheme(ThemeMode.dark);
                        },
                        modeName: 'Dark Mode',
                        icon: AppVectors.dartIcon,
                      )
                    ],
                  ),
                  const SizedBox(
                    height: 32,
                  ),
                  MainAppButton(
                    onTap: () {
                      Navigator.of(context).push(MaterialPageRoute(
                          builder: (context) => const AuthSelect()));
                    },
                    title: 'Continue',
                  ),
                  const SizedBox(
                    height: 54,
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
