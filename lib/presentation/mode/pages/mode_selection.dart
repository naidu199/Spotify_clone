import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:spotify/common/widgets/buttons/main_button.dart';
import 'package:spotify/common/widgets/buttons/mode_selection_button.dart';
import 'package:spotify/core/config/assets/app_images.dart';
import 'package:spotify/core/config/assets/app_vectors.dart';

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
                        onTap: () {},
                        icon: AppVectors.lightIcon,
                        modeName: 'Light Mode',
                      ),
                      ModeSelectionButton(
                        onTap: () {},
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
                          builder: (context) => const ModeSelection()));
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
