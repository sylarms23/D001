-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ovnis
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `ovnis` ;

-- -----------------------------------------------------
-- Schema ovnis
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ovnis` DEFAULT CHARACTER SET utf8 ;
USE `ovnis` ;

-- -----------------------------------------------------
-- Table `ovnis`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ovnis`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ovnis`.`sucesos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ovnis`.`sucesos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `lugar` VARCHAR(45) NULL,
  `descripcion` TEXT NULL,
  `fecha` DATE NULL,
  `ovnis` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_sucesos_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_sucesos_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `ovnis`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ovnis`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ovnis`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario_id` INT NOT NULL,
  `suceso_id` INT NOT NULL,
  `estado` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_likes_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  INDEX `fk_likes_sucesos1_idx` (`suceso_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `ovnis`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_sucesos1`
    FOREIGN KEY (`suceso_id`)
    REFERENCES `ovnis`.`sucesos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
