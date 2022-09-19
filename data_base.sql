-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema libros
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema libros
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `libros` DEFAULT CHARACTER SET utf8 ;
USE `libros` ;

-- -----------------------------------------------------
-- Table `libros`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `libros`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `libros`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `libros`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tittle` VARCHAR(255) NULL,
  `num_of_pages` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `libros`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `libros`.`favorites` (
  `book_id` INT NOT NULL,
  `author_id` INT NOT NULL,
  PRIMARY KEY (`book_id`, `author_id`),
  INDEX `fk_books_has_authors_authors1_idx` (`author_id` ASC) VISIBLE,
  INDEX `fk_books_has_authors_books_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_has_authors_books`
    FOREIGN KEY (`book_id`)
    REFERENCES `libros`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_books_has_authors_authors1`
    FOREIGN KEY (`author_id`)
    REFERENCES `libros`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
