package com.example.demo.student;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import java.time.LocalDate;
import java.time.Month;
import java.util.List;


@Configuration
public class StudentConfig {

    @Bean
    CommandLineRunner commandLineRunner(
            StudentRepository repository){
        return args -> {
            Student esther = new Student(
				1L,
				"Esther",
				"estherchu@gmail.com",
				LocalDate.of(2001, Month.FEBRUARY, 19)
			);
            Student john = new Student(
				"John",
				"ikjun@gmail.com",
				LocalDate.of(2000, Month.JULY, 27)
			);

            repository.saveAll(List.of(esther, john));
        };
    }

}
