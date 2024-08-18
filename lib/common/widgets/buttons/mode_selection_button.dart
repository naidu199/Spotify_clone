import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:spotify/core/config/theme/app_colors.dart';

class ModeSelectionButton extends StatelessWidget {
  final VoidCallback onTap;
  final double? height;
  final double? width;
  final String icon;
  final String modeName;
  const ModeSelectionButton(
      {super.key,
      required this.onTap,
      this.height,
      this.width,
      required this.modeName,
      required this.icon});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Column(
        children: [
          ClipOval(
            child: BackdropFilter(
              filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
              child: Container(
                height: height ?? 80,
                width: width ?? 80,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: const Color(0xff30393C).withOpacity(0.5),
                ),
                child: SvgPicture.asset(
                  icon,
                  fit: BoxFit.none,
                ),
              ),
            ),
          ),
          const SizedBox(
            height: 10,
          ),
          Text(
            modeName,
            style: const TextStyle(
                fontWeight: FontWeight.w500,
                fontSize: 17,
                color: AppColors.grey),
          )
        ],
      ),
    );
  }
}
