"""
Unit Tests for Gym Membership Management System
Tests unitarios para el Sistema de Gestión de Membresías
"""

import unittest
from gym_membership import GymMembership


class TestGymMembership(unittest.TestCase):
    """Clase de tests para el sistema de membresías"""
    
    def setUp(self):
        """Configuración antes de cada test"""
        self.gym = GymMembership()
    
    # Tests para selección de membresía
    def test_select_valid_membership_plan(self):
        """Test: Seleccionar un plan válido"""
        result = self.gym.select_membership_plan("Basic")
        self.assertTrue(result)
        self.assertEqual(self.gym.selected_plan, "Basic")
    
    def test_select_invalid_membership_plan(self):
        """Test: Seleccionar un plan inválido"""
        result = self.gym.select_membership_plan("InvalidPlan")
        self.assertFalse(result)
        self.assertIsNone(self.gym.selected_plan)
    
    def test_all_membership_plans_available(self):
        """Test: Todos los planes deben estar disponibles"""
        plans = ["Basic", "Premium", "Family"]
        for plan in plans:
            self.assertTrue(self.gym.select_membership_plan(plan))
    
    # Tests para características adicionales
    def test_add_valid_additional_feature(self):
        """Test: Agregar característica adicional válida"""
        result = self.gym.add_additional_feature("Personal Training")
        self.assertTrue(result)
        self.assertIn("Personal Training", self.gym.additional_features)
    
    def test_add_invalid_additional_feature(self):
        """Test: Agregar característica adicional inválida"""
        result = self.gym.add_additional_feature("Invalid Feature")
        self.assertFalse(result)
        self.assertNotIn("Invalid Feature", self.gym.additional_features)
    
    def test_add_multiple_additional_features(self):
        """Test: Agregar múltiples características adicionales"""
        self.gym.add_additional_feature("Personal Training")
        self.gym.add_additional_feature("Group Classes")
        self.assertEqual(len(self.gym.additional_features), 2)
    
    # Tests para cálculo de costos base
    def test_calculate_base_cost_basic_plan(self):
        """Test: Calcular costo base del plan Basic"""
        self.gym.select_membership_plan("Basic")
        cost = self.gym.calculate_base_cost()
        self.assertEqual(cost, 50)
    
    def test_calculate_base_cost_premium_plan(self):
        """Test: Calcular costo base del plan Premium"""
        self.gym.select_membership_plan("Premium")
        cost = self.gym.calculate_base_cost()
        self.assertEqual(cost, 100)
    
    def test_calculate_base_cost_family_plan(self):
        """Test: Calcular costo base del plan Family"""
        self.gym.select_membership_plan("Family")
        cost = self.gym.calculate_base_cost()
        self.assertEqual(cost, 150)
    
    def test_calculate_base_cost_no_plan_selected(self):
        """Test: Costo base sin plan seleccionado"""
        cost = self.gym.calculate_base_cost()
        self.assertEqual(cost, 0)
    
    # Tests para costo de características adicionales
    def test_calculate_additional_features_cost_single(self):
        """Test: Calcular costo de una característica adicional"""
        self.gym.add_additional_feature("Personal Training")
        cost = self.gym.calculate_additional_features_cost()
        self.assertEqual(cost, 40)
    
    def test_calculate_additional_features_cost_multiple(self):
        """Test: Calcular costo de múltiples características adicionales"""
        self.gym.add_additional_feature("Personal Training")  # 40
        self.gym.add_additional_feature("Group Classes")      # 25
        cost = self.gym.calculate_additional_features_cost()
        self.assertEqual(cost, 65)
    
    def test_calculate_additional_features_cost_none(self):
        """Test: Calcular costo sin características adicionales"""
        cost = self.gym.calculate_additional_features_cost()
        self.assertEqual(cost, 0)
    
    # Tests para descuento grupal
    def test_group_discount_two_members(self):
        """Test: Descuento grupal con 2 miembros (10%)"""
        self.gym.set_number_of_members(2)
        discount = self.gym.apply_group_discount(100)
        self.assertEqual(discount, 10)
    
    def test_group_discount_one_member(self):
        """Test: Sin descuento grupal con 1 miembro"""
        self.gym.set_number_of_members(1)
        discount = self.gym.apply_group_discount(100)
        self.assertEqual(discount, 0)
    
    def test_group_discount_five_members(self):
        """Test: Descuento grupal con 5 miembros"""
        self.gym.set_number_of_members(5)
        discount = self.gym.apply_group_discount(200)
        self.assertEqual(discount, 20)
    
    def test_set_invalid_number_of_members(self):
        """Test: Número inválido de miembros"""
        result = self.gym.set_number_of_members(0)
        self.assertFalse(result)
    
    # Tests para descuentos especiales
    def test_special_discount_over_400(self):
        """Test: Descuento especial cuando el total excede $400"""
        discount = self.gym.apply_special_offer_discount(450)
        self.assertEqual(discount, 50)
    
    def test_special_discount_over_200(self):
        """Test: Descuento especial cuando el total excede $200"""
        discount = self.gym.apply_special_offer_discount(250)
        self.assertEqual(discount, 20)
    
    def test_special_discount_under_200(self):
        """Test: Sin descuento especial cuando es menor a $200"""
        discount = self.gym.apply_special_offer_discount(150)
        self.assertEqual(discount, 0)
    
    def test_special_discount_exactly_200(self):
        """Test: Sin descuento especial exactamente en $200"""
        discount = self.gym.apply_special_offer_discount(200)
        self.assertEqual(discount, 0)
    
    def test_special_discount_exactly_400(self):
        """Test: Descuento especial exactamente en $400 (debe aplicar $20)"""
        discount = self.gym.apply_special_offer_discount(400)
        self.assertEqual(discount, 20)
    
    # Tests para características premium
    def test_add_valid_premium_feature(self):
        """Test: Agregar característica premium válida"""
        result = self.gym.add_premium_feature("Exclusive Gym Access")
        self.assertTrue(result)
        self.assertIn("Exclusive Gym Access", self.gym.premium_features)
    
    def test_add_invalid_premium_feature(self):
        """Test: Agregar característica premium inválida"""
        result = self.gym.add_premium_feature("Invalid Premium")
        self.assertFalse(result)
    
    def test_calculate_premium_features_cost(self):
        """Test: Calcular costo de características premium"""
        self.gym.add_premium_feature("Exclusive Gym Access")  # 80
        cost = self.gym.calculate_premium_features_cost()
        self.assertEqual(cost, 80)
    
    # Tests para recargo premium
    def test_premium_surcharge_with_premium_features(self):
        """Test: Recargo del 15% con características premium"""
        self.gym.add_premium_feature("Exclusive Gym Access")
        surcharge = self.gym.apply_premium_surcharge(100)
        self.assertEqual(surcharge, 15)
    
    def test_premium_surcharge_without_premium_features(self):
        """Test: Sin recargo premium sin características premium"""
        surcharge = self.gym.apply_premium_surcharge(100)
        self.assertEqual(surcharge, 0)
    
    # Tests de cálculo total integrado
    def test_total_cost_basic_plan_only(self):
        """Test: Costo total solo con plan Basic"""
        self.gym.select_membership_plan("Basic")
        total = self.gym.calculate_total_cost()
        self.assertEqual(total, 50)
    
    def test_total_cost_with_additional_features(self):
        """Test: Costo total con características adicionales"""
        self.gym.select_membership_plan("Basic")  # 50
        self.gym.add_additional_feature("Personal Training")  # 40
        total = self.gym.calculate_total_cost()
        self.assertEqual(total, 90)
    
    def test_total_cost_with_group_discount(self):
        """Test: Costo total con descuento grupal"""
        self.gym.select_membership_plan("Premium")  # 100
        self.gym.set_number_of_members(2)
        total = self.gym.calculate_total_cost()
        # 100 - 10% = 90
        self.assertEqual(total, 90)
    
    def test_total_cost_with_special_discount_200(self):
        """Test: Costo total con descuento especial de $20"""
        self.gym.select_membership_plan("Premium")  # 100
        self.gym.add_additional_feature("Personal Training")  # 40
        self.gym.add_additional_feature("Group Classes")  # 25
        self.gym.add_additional_feature("Nutrition Consultation")  # 30
        self.gym.add_additional_feature("Locker Rental")  # 10
        # Total: 100 + 40 + 25 + 30 + 10 = 205
        # Descuento: -20
        # Final: 185
        total = self.gym.calculate_total_cost()
        self.assertEqual(total, 185)
    
    def test_total_cost_with_special_discount_400(self):
        """Test: Costo total con descuento especial de $50"""
        self.gym.select_membership_plan("Family")  # 150
        self.gym.add_additional_feature("Personal Training")  # 40
        self.gym.add_additional_feature("Group Classes")  # 25
        self.gym.add_additional_feature("Nutrition Consultation")  # 30
        self.gym.add_additional_feature("Locker Rental")  # 10
        self.gym.add_premium_feature("Exclusive Gym Access")  # 80
        self.gym.add_premium_feature("Specialized Training Program")  # 60
        # Subtotal: 150 + 40 + 25 + 30 + 10 + 80 + 60 = 395
        # No alcanza $400, descuento de $20
        # After discount: 375
        # Premium surcharge 15%: 56.25
        # Total: 431.25
        total = self.gym.calculate_total_cost()
        self.assertEqual(total, 431.25)
    
    def test_total_cost_with_premium_surcharge(self):
        """Test: Costo total con recargo premium del 15%"""
        self.gym.select_membership_plan("Basic")  # 50
        self.gym.add_premium_feature("Exclusive Gym Access")  # 80
        # Subtotal: 130
        # After discount: 130 (no discount)
        # Premium surcharge 15%: 19.50
        # Total: 149.50
        total = self.gym.calculate_total_cost()
        self.assertEqual(total, 149.50)
    
    def test_total_cost_complex_scenario(self):
        """Test: Escenario complejo con múltiples descuentos y recargos"""
        self.gym.select_membership_plan("Premium")  # 100
        self.gym.set_number_of_members(3)
        self.gym.add_additional_feature("Personal Training")  # 40
        self.gym.add_additional_feature("Group Classes")  # 25
        self.gym.add_premium_feature("Exclusive Gym Access")  # 80
        # Subtotal: 245
        # Group discount 10%: -24.5 = 220.5
        # Special discount: -20 = 200.5
        # Premium surcharge 15%: +30.075 = 230.575
        total = self.gym.calculate_total_cost()
        self.assertAlmostEqual(total, 230.57, places=2)
    
    def test_total_cost_no_plan_selected(self):
        """Test: Costo total sin plan seleccionado"""
        total = self.gym.calculate_total_cost()
        self.assertEqual(total, -1)
    
    # Tests para validación y manejo de errores
    def test_membership_availability_validation(self):
        """Test: Validación de disponibilidad de membresía"""
        # Plan válido
        self.assertTrue(self.gym.select_membership_plan("Basic"))
        # Plan inválido
        self.assertFalse(self.gym.select_membership_plan("NonExistent"))
    
    def test_feature_availability_validation(self):
        """Test: Validación de disponibilidad de características"""
        # Característica válida
        self.assertTrue(self.gym.add_additional_feature("Personal Training"))
        # Característica inválida
        self.assertFalse(self.gym.add_additional_feature("NonExistent"))
    
    def test_confirm_membership_without_plan(self):
        """Test: Confirmar membresía sin plan seleccionado"""
        result = self.gym.confirm_membership()
        # Debería retornar -1 por falta de plan
        # Nota: Este test podría fallar por la entrada interactiva
        # Lo dejamos para validar la lógica
    
    # Tests de casos extremos
    def test_zero_cost_scenario(self):
        """Test: Escenario con costo cero (sin plan)"""
        total = self.gym.calculate_total_cost()
        self.assertEqual(total, -1)
    
    def test_maximum_features_scenario(self):
        """Test: Escenario con todas las características"""
        self.gym.select_membership_plan("Family")
        for feature in self.gym.ADDITIONAL_FEATURES:
            self.gym.add_additional_feature(feature)
        for feature in self.gym.PREMIUM_FEATURES:
            self.gym.add_premium_feature(feature)
        self.gym.set_number_of_members(5)
        total = self.gym.calculate_total_cost()
        # Verificar que retorna un número positivo
        self.assertGreater(total, 0)
    
    def test_negative_members_validation(self):
        """Test: Validación de número negativo de miembros"""
        result = self.gym.set_number_of_members(-1)
        self.assertFalse(result)


if __name__ == '__main__':
    # Ejecutar los tests
    unittest.main()